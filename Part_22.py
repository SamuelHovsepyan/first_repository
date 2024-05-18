try:
    file = open("kjhkjhgkjhgkjh")
    pass
except ZeroDivisionError:
    pass
except TypeError:
    pass
except IndexError:
    pass
except ValueError:
    pass
except ArithmeticError:
    pass
except Exception:
    pass
else:
    pass
finally:
    print("end of try/except")
    file.close()

 
file.close()
print("end of try/except")
