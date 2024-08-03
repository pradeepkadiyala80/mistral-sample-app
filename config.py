import logging

logging.basicConfig(
    file="output.log",
    encoding="utf-8",
    filemode="a",
    format="{levelname}: {name}: {message}", 
    style="{"
    datefmt="%Y-%m-%d %H:%M",
)