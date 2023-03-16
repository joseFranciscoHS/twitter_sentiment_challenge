import mysql.connector
from mysql.connector import Error
import json

try:
  cnx = mysql.connector.connect(host = 'localhost',
                                database = 'twitter',
                                user = 'root',
                                password = 'Elhe1005lore27**')
except mysql.connector.Error as err:
  if err.errno == Error.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == Error.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
#else:
  #cnx.close()

def extractTweet():
    tweets = [
    {
        "id": 1,
        "texto": "La tecnologia de la realidad virtual esta revolucionando la forma en que experimentamos los videojuegos. #tecnologia #videojuegos",
        "usuario": "gamers_unidos",
        "hashtags": ["tecnologia", "videojuegos"],
        "fecha": "2023-03-13 16:45:00",
        "retweets": 23,
        "favoritos": 87
    },
    {
        "id": 2,
        "texto": "Apple anuncia el lanzamiento de su nuevo iPhone 15 con camara mejorada y pantalla OLED de 6,7 pulgadas. #Apple #iPhone15",
        "usuario": "tech_news",
        "hashtags": ["Apple", "iPhone15"],
        "fecha": "2023-03-12 10:30:00",
        "retweets": 234,
        "favoritos": 1876
    },
    {
        "id": 3,
        "texto": "Google presenta su nuevo asistente virtual con inteligencia artificial que permite controlar el hogar desde el smartphone. #Google #hogarinteligente",
        "usuario": "tech_guru",
        "hashtags": ["Google", "hogarinteligente"],
        "fecha": "2023-03-11 15:20:00",
        "retweets": 78,
        "favoritos": 489
    },

    {
        "id": 4,
        "texto": "La empresa de tecnologia SpaceX anuncia el lanzamiento de su primer vuelo comercial a la luna. #SpaceX #vuelolunar",
        "usuario": "espaciofan",
        "hashtags": ["SpaceX", "vuelolunar"],
        "fecha": "2023-03-10 13:10:00",
        "retweets": 109,
        "favoritos": 732
    },

    {
        "id": 5,
        "texto": "El nuevo dron de DJI es capaz de grabar video en 8K y tiene un tiempo de vuelo de hasta 45 minutos. #drones #tecnologia",
        "usuario": "dron_adicto",
        "hashtags": ["drones", "tecnologia"],
        "fecha": "2023-03-09 17:05:00",
        "retweets": 45,
        "favoritos": 256
    },

    {
        "id": 6,
        "texto": "La empresa de tecnologia Nvidia lanza su nueva tarjeta grafica RTX 5080 con 24 GB de memoria y capacidad de ray tracing en tiempo real. #Nvidia #tarjetagrafica",
        "usuario": "pc_master_race",
        "hashtags": ["Nvidia", "tarjetagrafica"],
        "fecha": "2023-03-08 11:55:00",
        "retweets": 167,
        "favoritos": 1045
    },

    {
        "id": 7,
        "texto": "Nuevo iPhone 13 con pantalla de 120Hz",
        "usuario": "tech_news",
        "hashtags": ["iPhone", "tecnologia"],
        "fecha": "2022-02-27 10:20:30",
        "retweets": 50,
        "favoritos": 150
    },

    {
        "id": 8,
        "texto": "La proxima generación de procesadores Intel promete un gran avance en rendimiento",
        "usuario": "tech_world",
        "hashtags": ["Intel", "procesadores"],
        "fecha": "2022-02-26 08:30:15",
        "retweets": 120,
        "favoritos": 250
    },

    {
        "id": 9,
        "texto": "Samsung presenta su nuevo telefono plegable",
        "usuario": "smartphone_lover",
        "hashtags": ["Samsung", "telefonos plegables"],
        "fecha": "2022-02-25 15:45:00",
        "retweets": 30,
        "favoritos": 80
    },

    {
        "id": 10,
        "texto": "Apple presenta su nueva linea de MacBook Pro con chip M2",
        "usuario": "apple_news",
        "hashtags": ["MacBook", "Apple"],
        "fecha": "2022-02-24 12:10:05",
        "retweets": 80,
        "favoritos": 200
    },

    {
        "id": 11,
        "texto": "Google anuncia nuevas herramientas para desarrolladores de Android",
        "usuario": "android_dev",
        "hashtags": ["Android", "desarrollo"],
        "fecha": "2022-02-23 09:00:20",
        "retweets": 40,
        "favoritos": 100
    },

    {
        "id": 12,
        "texto": "Elon Musk anuncia un nuevo lanzamiento de cohetes de SpaceX",
        "usuario": "spacex_fan",
        "hashtags": ["SpaceX", "Elon Musk"],
        "fecha": "2022-02-22 14:30:45",
        "retweets": 120,
        "favoritos": 300
    },

    {
        "id": 13,
        "texto": "Microsoft lanza una actualizacion importante para Windows 11",
        "usuario": "windows_user",
        "hashtags": ["Windows", "actualizacion"],
        "fecha": "2022-02-21 11:40:10",
        "retweets": 60,
        "favoritos": 150
    },

	{
	"id": 14,
	"texto": "El gigante tecnologico Apple presenta su nueva linea de productos en un evento virtual. Entre las novedades se encuentran el nuevo iPhone y el Apple Watch Series 8. #AppleEvent #nuevosproductos",
	"usuario": "appleguru",
	"hashtags": ["AppleEvent", "nuevosproductos"],
	"fecha": "2023-03-11 10:30:00",
	"retweets": 652,
	"favoritos": 4121
	},

	{
	"id": 15,
	"texto": "La inteligencia artificial esta cada vez mas presente en nuestras vidas, ¿pero sabemos realmente como funciona? En nuestro ultimo articulo explicamos todo sobre esta tecnologia. #inteligenciaartificial #IA",
	"usuario": "tecnologiainfo",
	"hashtags": ["inteligenciaartificial", "IA"],
	"fecha": "2023-03-11 15:20:00",
	"retweets": 34,
	"favoritos": 93
	},

	{
	"id": 16,
	"texto": "La tecnologia blockchain esta revolucionando la forma en que se realizan las transacciones financieras. Descubre todo lo que necesitas saber sobre esta tecnologia en nuestro ultimo articulo. #blockchain #criptomonedas",
	"usuario": "criptoinfo",
	"hashtags": ["blockchain", "criptomonedas"],
	"fecha": "2023-03-12 09:45:00",
	"retweets": 51,
	"favoritos": 189
	},

	{
	"id": 17,
	"texto": "Los avances en tecnologia permiten crear prótesis cada vez mas sofisticadas y precisas. En nuestro ultimo articulo hablamos sobre algunos de los desarrollos más innovadores en este campo. #protesis #tecnologia",
	"usuario": "innovatech",
	"hashtags": ["protesis", "tecnologia"],
	"fecha": "2023-03-12 14:15:00",
	"retweets": 23,
	"favoritos": 64
	},

	{
	"id": 18,
	"texto": "La tecnologia de realidad aumentada se esta convirtiendo en una herramienta indispensable para los diseñadores de moda. Descubre como se esta utilizando esta tecnologia en nuestro ultimo artículo. #realidadaumentada #moda",
	"usuario": "fashiontech",
	"hashtags": ["realidadaumentada", "moda"],
	"fecha": "2023-03-13 11:00:00",
	"retweets": 45,
	"favoritos": 167
	},

	{
	"id": 19,
	"texto": "La tecnologia de reconocimiento facial esta siendo utilizada en muchos ambitos, pero ¿es realmente segura? En nuestro ultimo articulo analizamos los riesgos de esta tecnologia y como se pueden mitigar. #reconocimientofacial #seguridad",
	"usuario": "seguridadtech",
	"hashtags": ["reconocimientofacial", "seguridad"],
	"fecha": "2023-03-13 15:30:00",
	"retweets": 87,
	"favoritos": 312
	}, 

	{
	"id": 20,
	"texto": "La tecnologia 5G esta revolucionando la forma en que nos conectamos a internet. En nuestro ultimo articulo te explicamos todo lo que necesitas saber sobre esta nueva tecnologia. #tecnologia5G #internet",
	"usuario": "conexionveloz",
	"hashtags": ["tecnologia5G", "internet"],
	"fecha": "2023-03-14 10:00:00",
	"retweets": 75,
	"favoritos": 245
	},

	{
	"id": 21,
	"texto": "La tecnologia de la nube ha transformado la forma en que almacenamos y compartimos informacion. En nuestro ultimo articulo te explicamos todo lo que necesitas saber sobre esta tecnologia. #tecnologiadelanube #almacenamiento",
	"usuario": "cloudtech",
	"hashtags": ["tecnologiadelanube", "almacenamiento"],
	"fecha": "2023-03-14 14:30:00",
	"retweets": 40,
	"favoritos": 132
	},

	{
	"id": 22,
	"texto": "La tecnologia de la realidad virtual esta transformando la forma en que experimentamos el entretenimiento. En nuestro ultimo articulo te contamos todo lo que necesitas saber sobre esta tecnologia. #realidadvirtual #entretenimiento",
	"usuario": "entertech",
	"hashtags": ["realidadvirtual", "entretenimiento"],
	"fecha": "2023-03-15 09:15:00",
	"retweets": 52,
	"favoritos": 189
	},

	{
	"id": 23,
	"texto": "La tecnologia de los drones esta siendo utilizada en muchos ambitos, desde la entrega de paquetes hasta la vigilancia. En nuestro ultimo articulo te explicamos todo lo que necesitas saber sobre esta tecnologia. #drones #tecnologia",
	"usuario": "dronetech",
	"hashtags": ["drones", "tecnologia"],
	"fecha": "2023-03-15 15:00:00",
	"retweets": 29,
	"favoritos": 96
	},

	{
	"id": 24,
	"texto": "La tecnologia de la inteligencia artificial esta transformando la forma en que las empresas toman decisiones. En nuestro ultimo articulo te contamos todo lo que necesitas saber sobre esta tecnologia. #inteligenciaartificial #empresas",
	"usuario": "businessai",
	"hashtags": ["inteligenciaartificial", "empresas"],
	"fecha": "2023-03-16 11:20:00",
	"retweets": 62,
	"favoritos": 215
	},

	{
	"id": 25,
	"texto": "La tecnologia de la biometria esta siendo utilizada para mejorar la seguridad en muchos ambitos. En nuestro último articulo te explicamos todo lo que necesitas saber sobre esta tecnologia. #biometria #seguridad",
	"usuario": "biotech",
	"hashtags": ["biometria", "seguridad"],
	"fecha": "2023-03-16 16:45:00",
	"retweets": 47,
	"favoritos": 176
	}]

    dict_array = json.loads(json.dumps(tweets))
    tuple_array = [(d['id'], d['texto'], d['usuario'], tuple(d['hashtags']), d['fecha'], d['retweets'], d['favoritos']) for d in dict_array]
    print(tuple_array)


def createTable():
    try:
        mySql_Create_Table_Query = """
                                    DROP TABLE IF EXISTS TweetDB,
                                    CREATE TABLE IF NOT EXISTS TweetDB (
                                    IdTweet int(45) NOT NULL,
                                    Tweet varchar(290) NOT NULL,
                                    Username varchar(45)  NOT NULL,
                                    Hashtags set() NOT NULL,
                                    Datetime datetime NOT NULL,
                                    Retweets int(10),
                                    Favourites int(10),
                                    Rango set() NOT NULL,
                                    score float(11)  NULL,
                                    PRIMARY KEY (idTweet)
                                    );
                                    """

        cursor = cnx.cursor()
        result = cursor.execute(mySql_Create_Table_Query, multi=True)
        print("Tweet Table created successfully")                            

    except mysql.connector.Error as error:
            print("Failed to create table in MySQL", format(error))


def insertRowsIntoTable():
    try: 

        mySql_insert_Query = """INSERT INTO TweetDB (IdTweet, Tweet, Username, Hashtags, Datetime, Retweets, Favourites)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                                    
        records_to_insert = extractTweet()    
        
        cursor = cnx.cursor()
        cursor.executemany(mySql_insert_Query, records_to_insert)
        cnx.commit()
        print(cursor.rowcount, "Record inserted successfully into TweetDB table")                            

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")


def main():
    extractTweet()
    createTable()
    insertRowsIntoTable()

main()



