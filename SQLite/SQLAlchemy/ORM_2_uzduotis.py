# Su SQLAlchemy sukurkite modelį pagal šią diagramą:
# kurdami many2many ryšį nenaudokite association table, 
# vietoje jos sukurkite tarpinę lentelę kaip objektą


from sqlalchemy import create_engine, Integer, String, Float, ForeignKey, Column
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

db_engine = create_engine('sqlite:///ORM_du.db', echo=True)
session = sessionmaker(bind=db_engine)()


class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    f_name = Column("f_name", String(50))
    l_name = Column("l_name", String(50))
    email = Column("email", String(100))
    order = relationship("Order_", back_populates="customer")

    def __repr__(self):
        return f"{self.id}, {self.f_name}, {self.l_name}, {self.email}, {self.order}"
    

class Order_(Base):
    __tablename__ = "order_"
    id = Column(Integer, primary_key=True)
    customer_id = Column("customer_id", Integer, ForeignKey("customer.id"))
    date_ = Column("date_", String(50))
    products = relationship("ProductOrder", back_populates="order")
    status_id = Column("status_id", Integer, ForeignKey("status.id"))
    status = relationship("Status", back_populates="orders")
    customer = relationship("Customer", back_populates="order")

    def __repr__(self):
        return f"{self.id}, {self.customer_id}, {self.date_}, {self.products}, {self.status_id}, {self.status}, {self.customer}"

    
class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    name = Column("name", String(50))
    orders = relationship("Order_", back_populates="status")

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.orders}"
    

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column("name", String(50))
    price = Column("price", Float)
    orders = relationship("ProductOrder", back_populates="product")

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.price}, {self.orders}"
    
# Tarpine lentele ProductOrder
class ProductOrder(Base):
    __tablename__ = "product_order"
    id = Column(Integer, primary_key=True)
    order_id = Column("order_id", Integer, ForeignKey("order_.id"))
    product_id = Column("product_id", Integer, ForeignKey("product.id"))
    quantity = Column("quantity", Integer)
    order = relationship("Order_", back_populates="products")
    product = relationship("Product", back_populates="orders")

    def __repr__(self):
        return f"{self.id}, {self.order_id}, {self.product_id}, {self.quantity}, {self.order}, {self.product}"
    


# Parašykite programą, kuri naudojantis jūsų sukurtu modeliu leistų:
# Pridėti pirkėją
# Pridėti produktą
# Pridėti statusą
# Pridėti užsakymą
# Ištraukti užsakymą pagal id
# Pakeisti užsakymo statusą pagal užsakymo id
# Pridėti į užsakymą produktus su kiekiais



def add_customer(f_name, l_name, email):
    try:
        customer = Customer(f_name=f_name, l_name=l_name, email=email)
        session.add(customer)
        session.commit()
        print("Customer added successfully!")
        return customer
    except SQLAlchemyError as e:
        session.rollback()
        print("Failded to add customer:", str(e))
        
        
        
def add_product(name, price):
    try:
        product = Product(name=name, price=price)
        session.add(product)
        session.commit()
        print("Product added successfully!")
        return product
    except SQLAlchemyError as e:
        session.rollback()
        print("Failed to add product:", str(e))


def add_status(name):
    try:
        status = Status(name=name)
        session.add(status)
        session.commit()
        print("Status added successfully!")
        return status
    except SQLAlchemyError as e:
        session.rollback()
        print("Failed to add status:", str(e))


def add_order(customer_id, date_, status_id, product_id, quantity):
    try:
        order = Order_(customer_id=customer_id, date_=date_, status_id=status_id)
        session.add(order)
        session.commit()

        product_order = ProductOrder(order_id=order.id, product_id=product_id, quantity=quantity)
        session.add(product_order)
        session.commit()
        print("Order added successfully!")
        return order, product_order
    except SQLAlchemyError as e:
        session.rollback()
        print("Failed to add order:", str(e))


def get_order_by_id(order_id):
    try:
        order = session.query(Order_).get(order_id)
        if order:
            print(f"Order ID:{order.id}, Customer ID:{order.customer_id}, Date:{order.date_}, Status ID: {order.status_id}")
        else:
            print("Order not found.")
            return order
    except SQLAlchemyError as e:
        print("Failed to retrieve order:", str(e))


def update_order_status(order_id, status_id):
    try:
        order = session.query(Order_).get(order_id)
        if order:
            order.status_id = status_id
            session.commit()
            print("Order status updated successfully!")
        else:
            print("Order not found.")
            return order
    except SQLAlchemyError as e:
        session.rollback()
        print("Failed to update order status:", str(e))


def add_product_to_order():
    try:
        order_id = session.query(Order_).all()[-1].id # Parodo paskutini lenteles ID
        id = int(input(f"Order ID (1-{order_id}):c"))
        order_ = session.get(Order_, id) # Gaunami visi irasai susieti su ID
        product_maxid = session.query(Product).order_by(Product.id.desc()).first().id
        product_id = int(input(f"Product ID (1 - {product_maxid}):"))
        quantity = int(input("Insert product quantity:"))
        order_.products.append(session.get(Product, product_id))
        order_product = ProductOrder(order_id=order_id, product_id=product_id, quantity=quantity)
        session.add(order_product)
    except SQLAlchemyError as e:
        print(f"Errors: {e}")
    else:
        session.commit()
        print(f"Product successfully added to Order")

    
# def add_product_to_order(order_id, product_quantities):
#     try:
#         order = session.query(Order_).get(order_id)
#         if order:
#             for product_id, quantity in product_quantities.items():
#                 product_order = ProductOrder(order_id=order.id, product_id=product_id, quantity=quantity)
#                 session.add(product_order)
#             session.commit()
#             print("Products added to order successfully!")
#             return order
#         else:
#             print("Order not found!")
#     except SQLAlchemyError as e:
#         session.rollback()
#         print("Failed to add products to order:", str(e))



############################################################################################################


if __name__ == "__main__":
    Base.metadata.create_all(db_engine)
    
    while True:
        option = int(input("""====Order App, choose action:====
        1 - Add customer,
        2 - Add product,
        3 - Add status,
        4 - Add order,
        7 - Get order by ID,
        8 - Update order status,
        9 - Add product to order, 
        0 - Close program."""))

        try:
            option = int(option)
        except:
            pass
        
        if option == 1:
            f_name = input("Enter first name:")
            l_name = input("Enter last name:")
            email = input("Enter email:")
            add_customer(f_name, l_name, email)
        
        elif option == 2:
            name = input("Enter product name:")
            price = float(input("Enter product price:"))
            add_product(name, price)

        elif option ==3:
            name = input("Enter order status:")
            add_status(name)

        elif option == 4:
            customer_id = int(input("Enter customer ID:"))
            date_ = input("Enter order date:")
            status_id = int(input("Enter status ID:"))
            product_id = int(input("Enter product ID:"))
            quantity = int(input("Enter quantity:"))
            add_order(customer_id, date_, status_id, product_id, quantity)
        
        elif option == 7:
            order_id = int(input("Enter order ID:"))
            get_order_by_id(order_id)

        elif option == 8:
            order_id = int(input("Enter order ID:"))
            status_id = int(input("Enter new status ID:"))
            update_order_status(order_id, status_id)

        elif option == 9:
            order_id = int(input("Enter order ID:"))
            product_quantities = {}
            num_products = int(input("Enter the number of products:"))
            for i in range(num_products):
                product_id = int(input("Enter product ID:"))
                quantity = int(input("Enter quantity:"))
                product_quantities[product_id] = quantity
            add_product_to_order(order_id, product_quantities)

        elif option == 0: 
            print("====Program closed...====")
            break

        










