**Flour and love Bakery Management System**

## Description

This project involves the development of a management system for a bakery to efficiently handle products, orders, and related details. The system will facilitate the administration of available products (such as bread, cakes, and pastries), record customer orders, and manage order-specific details. The goal is to optimize inventory control, ensure accurate pricing, and enhance the customer experience.

## Problem Statement

The bakery "**Flour and Love Bakery**" faces challenges related to inventory management and order processing. Currently, products and orders are recorded manually, leading to human errors, data loss, and difficulties in tracking order details. The bakery requires a digital system that centralizes information, provides effective inventory control, and records each order in an organized manner.

## Tools

- **Resource**: [Google Drive Folder](https://drive.google.com/drive/folders/1sgEohHBFul6AjnAziCO5zaqb4YNQ8BFQ?usp=sharing)

## Features

### **Product Management**
- Registration of bakery products such as bread, cakes, and pastries.
- Storage of relevant information including product name, category (bread, cake, pastry), description, supplier, stock quantity, purchase price, and sale price.

### **Order Management**
- Creation of new orders by customers.
- Registration of products within an order, including quantity, unit price, and order line details.
- Ability to edit and delete orders.

### **Automated Inventory**
- Automatic stock reduction when an order is placed.
- Stock control and alerts when a product is running low.

### **Search & Queries**
- Search for products by name, category, or code.
- Filter orders by order code or included products.

### **File Handling & Data Persistence**
- Data storage in JSON files to ensure information persistence across sessions.

## System Structure Overview

- **Products**: Dictionary containing product code, name, category, supplier, stock quantity, and prices.
- **Orders**: Dictionary containing order code, customer code, order date, and a list of order details.
- **Order Details**: Includes product code, requested quantity, unit price, and line number within the order.

## Technical Considerations

- **Persistence**: Data will be stored and managed using JSON files.
- **Modularity**: The system will be organized into modular functions for product and order management, as well as file handling.
- **Validation**: Implementations will ensure unique product and order codes, as well as stock availability verification before processing an order.

## Requirements

- Python 3.x
- JSON library for data handling
- Tabulate library for tables control
- GitHub for version control

### Installation
To install the `tabulate` library, follow these steps:

#### Using pip 
```bash
pip install tabulate
```



## Best Practices

- Use modular functions for better code clarity and reusability.
- Implement clear and descriptive variable and function names.
- Validate user input to prevent errors and ensure data integrity.

## Example Execution

```
"""
𝐵𝐼𝐸𝑁𝑉𝐸𝑁𝐼𝐷𝑂𝑆 𝐴𝐿 𝑃𝑂𝑅𝑇𝐴𝐿 𝑈𝑆𝑈𝐴𝑅𝐼𝑂
1.Generar nuevo pedido.
2.Inventario de productos.
3.Administrar pedidos.
4.Salir del portal usuario..

"""

"""
𝐼𝑁𝑉𝐸𝑁𝑇𝐴𝑅𝐼𝑂 𝑃𝑅𝑂𝐷𝑈𝐶𝑇𝑂𝑆
1.Ver lista productos.
2.Ver lista productos agrupados por categoria.
3.Actualizar inventario de un producto.
4.Agregar o eliminar un producto del inventario.
5.Buscar producto por nombre.
6.Buscas producto por codigo.
7.Regresar al menu principal.

"""

"""
𝐴𝐷𝑀𝐼𝑁𝐼𝑆𝑇𝑅𝐴𝑅 𝑃𝐸𝐷𝐼𝐷𝑂𝑆
1.Editar pedido.
2.Eliminar pedido.
3.Ver historial de pedidos.
4.Ver pedido por codigo.
5.Regresar al menu principal.

"""

"""
𝐼𝑁𝑉𝐸𝑁𝑇𝐴𝑅𝐼𝑂 𝑃𝑅𝑂𝐷𝑈𝐶𝑇𝑂
1.Añadir producto.
2.Descontar producto.
3.Regresar al menu inventario.

"""

"""
𝐸𝐷𝐼𝑇𝐴𝑅 𝑃𝐸𝐷𝐼𝐷𝑂𝑆
1.Remover un producto del pedido.
2.Editar el stock de un producto en el pedido.
3.Regresar al menu administrar pedidos.

"""

"""
𝐸𝐷𝐼𝑇𝐴𝑅 𝑃𝑅𝑂𝐷𝑈𝐶𝑇𝑂𝑆 𝐷𝐸𝐿 𝐼𝑁𝑉𝐸𝑁𝑇𝐴𝑅𝐼𝑂
1.Agregar un producto nuevo
2.Eliminar un producto del inventario
3.Regresar al menu inventario.

"""
```

## Authors

- Developed by **Dylan Acevedo**

