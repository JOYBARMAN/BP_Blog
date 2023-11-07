from colorlog.formatter import ColoredFormatter


class CustomFormatter(ColoredFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, log_colors=None)
        self.log_colors = {
            "DEBUG": "white",
            "INFO": "bold_purple",
            "WARNING": "bold_blue",
            "ERROR": "bold_red",
            "CRITICAL": "bold_red",
        }
