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
    
#insert item in dynamodb table
def insert_item_dynamodb(nombre_tabla, id, nombre, apellido):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.put_item(
        Item={
            'id': id,
            'nombre': nombre,
            'apellido': apellido
        }
        )
    print("Se insertó el elemento correctamente")
    
#leer los elementos de una tabla de dynamodb
def leer_elementos_dynamodb(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    response = table.scan()
    items = response['Items']
    for item in items:
        print(item)
        

#eliminar elemento de una tabla de dynamodb
def eliminar_elemento_dynamodb(nombre_tabla, id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.delete_item(
        Key={
            'id': id
        }
    )
    print("Se eliminó el elemento correctamente")
    
#reconocer celebridad en imagen
def reconocer_celebridad_imagen(imagen):
    rekognition = boto3.client('rekognition')
    response = rekognition.recognize_celebrities(Image={'Bytes': imagen})
    print(response['CelebrityFaces'][0]['Name'])
        
opcion = 1

while opcion != 0:
    print("Ingrese la opción que desea")
    print("1. Listar tablas de dynamodb de la cuenta")
    print("2. Crear nueva tabla")
    print("3. Insertar elemento en tabla")
    print("4. Leer los elementos de una tabla")
    print("5. Eliminar elemento de una tabla")
    print("6. Reconocer celebridad en imagen")
    print("0. Salir")
    opcion = int(input())
    if opcion == 1:
        listar_tablas()  
    elif opcion == 2:
        nombre_tabla = input("Ingrese el nombre de la tabla")
        crear_tabla_dynamodb(nombre_tabla)
    elif opcion == 3:
        nombre_tabla = input("Ingrese el nombre de la tabla")
        iid = input("Ingrese el id del elemento")
        inombre = input("Ingrese el nombre del elemento")
        iapellido = input("Ingrese el apellido del elemento")
        insert_item_dynamodb(nombre_tabla, iid, inombre, iapellido)
    elif opcion == 4:
        nombre_tabla = input("Ingrese el nombre de la tabla")
        leer_elementos_dynamodb(nombre_tabla)
    elif opcion == 5:
        nombre_tabla = input("Ingrese el nombre de la tabla")
        iid = input("Ingrese el id del elemento")
        eliminar_elemento_dynamodb(nombre_tabla, iid)
    elif opcion == 6:
        #convertir imagen a bytes
        with open("IMAGEN.jpeg", "rb") as f:
            imagen = f.read()
            reconocer_celebridad_imagen(imagen)
    elif opcion == 0:
        print("Hasta luego")
    else:
        print("Opción no válida")