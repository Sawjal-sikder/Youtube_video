# Django REST Framework with drf-spectacular

This project demonstrates how to integrate **drf-spectacular** with Django REST Framework to automatically generate OpenAPI 3.0 documentation for your API.

## What is drf-spectacular?

`drf-spectacular` is a sane and flexible OpenAPI 3.0 schema generation library for Django REST Framework. It automatically generates comprehensive API documentation from your DRF views, serializers, and models.

## Features

- ✅ Automatic OpenAPI 3.0 schema generation
- ✅ Interactive Swagger UI for API testing
- ✅ Beautiful ReDoc documentation interface
- ✅ Customizable API documentation
- ✅ Support for authentication, permissions, and filtering
- ✅ Real-time schema updates as you modify your API

## Installation

1. Install the package:
```bash
pip install drf-spectacular
```

2. Add to your `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    # ... other apps
    "rest_framework",
    "drf_spectacular",
]
```

3. Configure REST Framework to use spectacular's schema generator:
```python
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

4. Add drf-spectacular settings:
```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
```

5. Add URLs to your `urls.py`:
```python
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
```
urlpatterns
```
urlpatterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

## Usage

### Starting the Development Server

```bash
python manage.py runserver
```

### Accessing Documentation

Once your server is running, you can access the API documentation at:

| Interface | URL | Description |
|-----------|-----|-------------|
| **Swagger UI** | http://127.0.0.1:8000/api/schema/swagger-ui/ | Interactive API documentation with testing capabilities |
| **ReDoc** | http://127.0.0.1:8000/api/schema/redoc/ | Beautiful, responsive API documentation |
| **OpenAPI Schema** | http://127.0.0.1:8000/api/schema/ | Raw OpenAPI 3.0 schema in JSON format |

### Example API Endpoints

The documentation will automatically include all your DRF endpoints. For example:

- `GET /api/products/` - List all products
- `POST /api/products/` - Create a new product
- `GET /api/products/{id}/` - Retrieve a specific product
- `PUT /api/products/{id}/` - Update a product
- `DELETE /api/products/{id}/` - Delete a product

## Customization

### Adding Custom Schema Information

You can enhance your API documentation by adding docstrings and using drf-spectacular decorators:

```python
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing products.
    
    This endpoint allows you to create, read, update, and delete products.
    """
    
    @extend_schema(
        summary="List all products",
        description="Retrieve a list of all products in the system",
        parameters=[
            OpenApiParameter(
                name='category',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Filter products by category'
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
```

### Customizing Settings

Update your `SPECTACULAR_SETTINGS` to customize the documentation:

```python
SPECTACULAR_SETTINGS = {
    'TITLE': 'Your API Title',
    'DESCRIPTION': 'Your API description',
    'VERSION': '1.0.0',
    
    # Optional: Add contact information
    'CONTACT': {
        'name': 'Your Name',
        'email': 'your-email@example.com',
        'url': 'https://yourwebsite.com',
    },
    
    # Optional: Add license information
    'LICENSE': {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT',
    },
    
    # UI Customizations
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': False,
        'filter': True,
        'requestSnippets': True,
    },
    
    # Security schemes
    'SECURITY': [{'type': 'http', 'scheme': 'bearer'}],
    
    # Component customization
    'COMPONENT_SPLIT_REQUEST': True,
    'COMPONENT_NO_READ_ONLY_REQUIRED': True,
}
```

## Advanced Features

### Authentication Documentation

If you're using authentication, drf-spectacular will automatically document your security schemes:

```python
# In your view
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # Your view logic
```

### Custom Serializer Fields

Document custom fields with proper OpenAPI types:

```python
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

@extend_schema_field(OpenApiTypes.URI)
class CustomURLField(serializers.Field):
    def to_representation(self, value):
        # Your custom logic
        pass
```

### Filtering and Pagination

drf-spectacular automatically documents DRF filters and pagination:

```python
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']
    pagination_class = PageNumberPagination
```

## Tips and Best Practices

1. **Use Docstrings**: Add clear docstrings to your views and serializers
2. **Use Type Hints**: Python type hints improve schema generation
3. **Custom Examples**: Use `@extend_schema` to provide request/response examples
4. **Organize Endpoints**: Use tags to group related endpoints
5. **Version Your API**: Include version information in your schema

## Troubleshooting

### Common Issues

1. **Schema not updating**: Restart your development server after making changes
2. **Missing endpoints**: Ensure your views are properly registered in URLs
3. **Authentication issues**: Check your `REST_FRAMEWORK` authentication settings

### Debug Mode

Enable debug mode to see detailed schema generation information:

```python
SPECTACULAR_SETTINGS = {
    # ... other settings
    'DEBUG': True,  # Only for development
}
```

## Additional Resources

- [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/)
- [OpenAPI 3.0 Specification](https://swagger.io/specification/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)

## Project Structure

```
core/
├── manage.py
├── README.md
├── db.sqlite3
├── core/
│   ├── __init__.py
│   ├── settings.py      # drf-spectacular configuration
│   ├── urls.py          # documentation URLs
│   └── wsgi.py
└── product/
    ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── views.py         # API endpoints
    └── urls.py
```

---

**Happy API documenting! 🚀**
