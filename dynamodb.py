import boto3

#crear funcion para listar tablas de dynamodb
def listar_tablas():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
        
#crear funcion para crear tabla de dynamodb con capacidad bajo demanda
def crear_tabla_dynamodb(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=nombre_tabla,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )
    print("Tabla creada exitosamente")
        
        
opcion = 1

while opcion != 0:
    print("Ingrese la opción que desea")
    print("1. Listar tablas de dynamodb de la cuenta")
    print("2. Crear nueva tabla")
    print("0. Salir")
    opcion = int(input())
    if opcion == 1:
        listar_tablas()  
    elif opcion == 2:
        nombre_tabla = input("Ingrese el nombre de la tabla")
        crear_tabla_dynamodb(nombre_tabla)
    elif opcion == 0:
        print("Hasta luego")
    else:
        print("Opción no válida")