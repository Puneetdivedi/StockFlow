from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from typing import List

from .. import schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Order, status_code=status.HTTP_201_CREATED)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Verify customer exists
    customer = db.query(models.Customer).filter(models.Customer.id == order.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Prepare to calculate total and check stock
    total_amount = 0.0
    product_updates = []  # (product_obj, new_stock)
    order_items = []

    for item in order.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).with_for_update().first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for product {product.sku}. Available: {product.stock_quantity}, Requested: {item.quantity}",
            )
        # Calculate line total
        line_total = item.quantity * product.price
        total_amount += line_total
        # Reduce stock
        new_stock = product.stock_quantity - item.quantity
        product_updates.append((product, new_stock))
        # Prepare OrderItem instance
        order_item = models.OrderItem(
            product_id=product.id,
            quantity=item.quantity,
            unit_price=product.price,
        )
        order_items.append(order_item)

    # Create Order record
    db_order = models.Order(
        customer_id=customer.id,
        total_amount=total_amount,
        items=order_items,
    )
    db.add(db_order)

    # Apply stock updates
    for product, new_stock in product_updates:
        product.stock_quantity = new_stock
        db.add(product)

    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Order).offset(skip).limit(limit).all()

@router.get("/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    # Restore stock before deletion
    for item in order.items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if product:
            product.stock_quantity += item.quantity
            db.add(product)
    db.delete(order)
    db.commit()
    return None
