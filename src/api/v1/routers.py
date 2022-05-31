from src.api.v1.endpoints import telegram, stats, forms


routers = {
    "/bot": telegram.router,
    "/api/stats": stats.router,
    "/api/forms": forms.router
}