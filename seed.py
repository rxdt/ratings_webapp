import model
from model import User, Movie, Rating
import sys, csv, datetime

def load_users(session):
    with open('seed_data/u.user', 'rb') as f:
        reader = csv.reader(f, delimiter='|')
        try:
            for row in reader:
                # row.rstrip()
                u = User(id=row[0], age=row[1], zipcode=row[4])
                session.add(u)
        except (csv.Error) as e:
            print "ROXANA RXANA ROXANA ROXANA"
            sys.exit('file %s, line %d: %s' % (u.user, reader.line_num, e))

        session.commit()

def load_movies(session):
    # use u.item
    with open('seed_data/u.item', 'rb') as f:
        reader = csv.reader(f, delimiter='|')
        try:
            for row in reader:

                name = row[1].rsplit(' ', 1)[0]
                name = name.decode("latin-1")

                if row[2] is not '':
                    date = datetime.datetime.strptime(row[2], "%d-%b-%Y")
                    m = Movie(id=row[0], name=name, release_date=date, imdb_url=row[4])
                    session.add(m)
        except (csv.Error, TypeError) as e:
            sys.exit('file %s, line %d: %s' % (m.item, reader.line_num, e))

        session.commit()

def load_ratings(session):
    with open('seed_data/u.data', 'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        try:
            for row in reader:
                r = Rating(user_id=row[0], movie_id=row[1], rating=row[2])
                session.add(r)
        except (csv.Error, TypeError, sqlalchemy.exc.IntegrityError) as e:
            print "ROXANA RXANA ROXANA ROXANA"
            sys.exit('file %s, line %d: %s' % (r.user, reader.line_num, e))

        session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session)
    # load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)

