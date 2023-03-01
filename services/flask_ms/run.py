from app import create_app

# Selecciona la configuración deseada (p.ej. 'development')
config_name = 'development'

# Crea la instancia de la aplicación
app = create_app(config_name)

if __name__ == '__main__':
    # Inicia la aplicación
    app.run()