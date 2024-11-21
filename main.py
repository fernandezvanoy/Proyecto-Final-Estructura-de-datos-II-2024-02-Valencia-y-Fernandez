class MotorDatosNoSQL:

    def __init__(self):
        self.tabla_documentos = {}

    def insert_field(self, id_document, field_key, field_value):
        if id_document not in self.tabla_documentos:
            self.tabla_documentos[id_document] = {}
        document = self.tabla_documentos[id_document]
        if field_key in document:
            print("Error: El campo ya existe en el documento.")
            return
        document[field_key] = field_value
        print("Campo insertado en el documento.")

    def update_field(self, id_document, field_key, new_value):
        if id_document not in self.tabla_documentos or field_key not in self.tabla_documentos[id_document]:
            print("Error: Documento o campo no encontrado.")
            return
        self.tabla_documentos[id_document][field_key] = new_value
        print("Campo actualizado en el documento.")

    def get_field(self, id_document, field_key):
        if id_document in self.tabla_documentos and field_key in self.tabla_documentos[id_document]:
            print(f"Valor: {self.tabla_documentos[id_document][field_key]}")
        else:
            print("Error: Documento o campo no encontrado.")

    def delete_field(self, id_document, field_key):
        if id_document in self.tabla_documentos and field_key in self.tabla_documentos[id_document]:
            del self.tabla_documentos[id_document][field_key]
            print("Campo eliminado del documento.")
        else:
            print("Error: Documento o campo no encontrado.")

    def list_document(self, id_document):
        if id_document in self.tabla_documentos:
            print(f"Documento {id_document}:")
            for field_key, field_value in self.tabla_documentos[id_document].items():
                print(f"  Campo: {field_key} | Valor: {field_value}")
        else:
            print("Error: Documento no encontrado.")

    def list_all(self):
        if not self.tabla_documentos:
            print("No hay documentos.")
            return
        for id_document, fields in self.tabla_documentos.items():
            print(f"Documento {id_document}:")
            for field_key, field_value in fields.items():
                print(f"  Campo: {field_key} | Valor: {field_value}")


def ejecutar_comando(base_datos, comando):
    parts = comando.split()
    accion = parts[0]

    if accion == "INSERT_FIELD":
        id_document, field_key, field_value = parts[1], parts[2], parts[3]
        base_datos.insert_field(id_document, field_key, field_value)
    elif accion == "UPDATE_FIELD":
        id_document, field_key, field_value = parts[1], parts[2], parts[3]
        base_datos.update_field(id_document, field_key, field_value)
    elif accion == "GET_FIELD":
        id_document, field_key = parts[1], parts[2]
        base_datos.get_field(id_document, field_key)
    elif accion == "DELETE_FIELD":
        id_document, field_key = parts[1], parts[2]
        base_datos.delete_field(id_document, field_key)
    elif accion == "LIST_DOCUMENT":
        id_document = parts[1]
        base_datos.list_document(id_document)
    elif accion == "LIST_ALL":
        base_datos.list_all()
    else:
        print("Comando no reconocido")


def main():
    base_datos = MotorDatosNoSQL()
    print("Ingrese comandos:")

    while True:
        comando = input("> ")
        if comando == "SALIR":
            break
        ejecutar_comando(base_datos, comando)


if __name__ == "__main__":
    main()