import uvicorn
import os

from routes import router

app = FastAPI()

app.include_router(router)

uvicorn.run(
    app,
    host="0.0.0.0",
    port=8000,
    reload=True,
    reload_dirs=[os.path.dirname(os.path.abspath(__file__))],
    reload_excludes=[
        "*/.git/*",
        "*/__pycache__/*",
        "*.pyc",
        "*/.pytest_cache/*",
        "*/.vscode/*",
        "*/.idea/*"
    ],
    reload_delay=1,
    reload_includes=["*.py", "*.html", "*.css", "*.js"]
)