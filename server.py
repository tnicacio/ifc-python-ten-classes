from config import app, db

# import os
# from config import db_file

if __name__ == "__main__":

    # if os.path.exists(db_file):
    #     os.remove(db_file)

    from controller import *

    db.create_all()

    app.run(debug=True, host='0.0.0.0')
