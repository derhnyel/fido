from core.config import config




if __name__ == "__main__":
    def number_of_workers():
            return (multiprocessing.cpu_count() * 2) + 1
    # Gunicorn configuration
    if config.ENVIRONMENT == "production":
        import multiprocessing

        import gunicorn.app.base

        class Gunicorn(gunicorn.app.base.BaseApplication):
            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super().__init__()

            def load_config(self):
                config = {
                    key: value
                    for key, value in self.options.items()
                    if key in self.cfg.settings and value is not None
                }
                for key, value in config.items():
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        options = {
            "bind": f"{config.host}:{config.port}",
            "workers": config.workers or number_of_workers(),
            "worker_class": "uvicorn.workers.UvicornWorker",
            "reload": False,
        }
        Gunicorn(config.app, options).run()
    else:
        import uvicorn

        uvicorn.run(
            app=config.app,
            host=config.host,
            reload=True if config.ENVIRONMENT == "development" else False,
            workers=config.workers or number_of_workers(),
            port=config.port,
            log_level=config.log_level,
        )
