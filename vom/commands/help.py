import tkinter as tk
from tkinter import ttk
import functools

from vom.resources.scripts.string import String

def help(args: list[str]) -> None:
    print(String.repo.readMeContent())