import os

if __name__ == "__main__":

        try:

                __import__("H3diIG").login()

        except Exception as e:

                exit(str(e))
