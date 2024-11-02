Este repositorio nace de seguir el video tutorial  de Brais Moure, que realiza con Reflex, que es un framework de pyton para desarrollo web. No tiene mayor pretensión.
Pasos para iniciar un proyecto con reflex:
En la consola posicionarse en la carpeta raiz del proyecto.
A continuacion ejecutar: 
reflex init (para instalar reflex en la carpeta)

PS C:\Users\fcoja\almacen_reflex> reflex init      
───────────────────────────────── Initializing almacen_reflex ──────────────────────────────────
Warning: Your version (0.5.10) of reflex is out of date. Upgrade to 0.6.4 with 'pip install 
reflex --upgrade'
Invalid XSL format (or) file name.
The command `wmic cpu get addresswidth,caption,manufacturer /FORMAT:csv` failed with error:     
Command 'wmic cpu get addresswidth,caption,manufacturer /FORMAT:csv' returned non-zero exit     
status 44210.. This will return None.
Warning: Bun for Windows is currently only available for x86 64-bit Windows. Installation will 
fall back on npm.
[08:44:51] Initializing the web directory.                                        console.py:104

Get started with a template:
(0) blank (https://blank-template.reflex.run) - A minimal template
(1) dashboard (https://dashboard-new.reflex.run/) - A dashboard with tables and graphs
(2) sales (https://sales-new.reflex.run/) - An app to manage sales and customers
(3) ai_image_gen (https://ai-image-gen.reflex.run/) - An app to generate images using AI        
(4) ci_template (https://cijob.reflex.run/) - A template for continuous integration
(5) api_admin_panel (https://api-admin-panel.reflex.run/) - An admin panel for an api.
(6) nba (https://nba-new.reflex.run/) - A data visualization app for NBA data.
(7) customer_data_app (https://customer-data-app.reflex.run/) - An app to manage customer data. 
Which template would you like to use? (0): 0
[08:45:26] Initializing the app directory.                                        console.py:104
Success: Initialized almacen_reflex

PS C:\Users\fcoja\almacen_reflex> py -m ent_vir_reflex (para crear un entorno virtual donde se trabajará en la aplicación)

PS C:\Users\fcoja\almacen_reflex> cd ent_vir_reflex  (entramos en el directorio principal del entorno virtual)

PS C:\Users\fcoja\almacen_reflex\ent_vir_reflex> Scripts\activate(ejecutamos este comando)

(ent_vir_reflex) PS C:\Users\fcoja\almacen_reflex\ent_vir_reflex> (ya estamos en nuestro entorno virtual)



