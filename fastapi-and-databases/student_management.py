from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint, select, insert, update, delete

# 1. DB Connection
engine = create_engine("mysql+pymysql://root:Krishn%40B04@localhost/student_db")

metadata = MetaData()

# 2. Table Creation
students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("age", Integer),
    Column("city", String(50), nullable=True),
    CheckConstraint("age >= 18")
)

metadata.create_all(engine)

conn = engine.connect()

# 3. Insert Data
conn.execute(insert(students), [
    {"name": "Rahul", "age": 22, "city": "Pune"},
    {"name": "Amit", "age": 19, "city": "Mumbai"},
    {"name": "Neha", "age": 20, "city": "Delhi"}
])
conn.commit()

# 4. Fetch All
print("\nAll Students:")
result = conn.execute(select(students))
for row in result:
    print(row)

# 5. Update Rahul's city
conn.execute(
    update(students)
    .where(students.c.name == "Rahul")
    .values(city="Bangalore")
)
conn.commit()

print("\nAfter Update:")
result = conn.execute(select(students))
for row in result:
    print(row)

# 6. Delete students with age < 20
conn.execute(delete(students).where(students.c.age < 20))
conn.commit()

print("\nAfter Deletion:")
result = conn.execute(select(students))
for row in result:
    print(row)

conn.close()