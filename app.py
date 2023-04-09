# app.py
import os

print(os.getenv("test"))


if os.path.exists("env.py"):
    import env

print(os.getenv("envpy_test"))
