🖨️ PrintFlow

Sistema de gestión de trabajos de impresión desarrollado en Python.

PrintFlow permite administrar clientes y pedidos de impresión desde una aplicación de consola, guardando la información de forma persistente mediante archivos JSON.

## 🚀 Funcionalidades actuales

✅ Registrar clientes  
✅ Guardar información automáticamente  
✅ Consultar lista de clientes  
✅ Registrar tipo de trabajo solicitado  
✅ Gestionar estados de pedidos:
- Pendiente
- En proceso
- Finalizado
- Entregado

✅ Actualización del estado de producción  
✅ Registro automático de fecha de creación  
✅ Registro automático de fecha de entrega  
✅ Archivado de clientes entregados  
✅ Consulta de clientes archivados  
✅ Resumen de clientes e ingresos:
- Clientes activos
- Clientes archivados
- Total histórico
- Ingresos activos
- Ingresos históricos
- Ingresos totales

🛠️ Tecnologías utilizadas

🐍 Python 3.14
🗄️ JSON para almacenamiento de datos
🌿 Git
☁️ GitHub
💻 Visual Studio Code
📂 Estructura del proyecto

PrintFlow/
│
├── main.py                    # Código principal de la aplicación
├── clientes.json              # Clientes activos
├── clientes_archivados.json   # Historial de clientes entregados
├── README.md                  # Documentación del proyecto
└── .gitignore

▶️ Cómo ejecutar el proyecto

Clonar el repositorio:
git clone https://github.com/Evienne22/PrintFlow.git
Entrar a la carpeta:
cd PrintFlow
Ejecutar:
python main.py
## 📌 Próximas mejoras

- Agregar generación de reportes PDF
- Migrar almacenamiento a SQLite
- Crear una interfaz web con FastAPI
- Implementar sistema de usuarios
- Agregar estadísticas avanzadas

---

## 👨‍💻 Autor

Diego Olivera

Proyecto realizado como práctica de desarrollo de software y gestión de pedidos de impresión.