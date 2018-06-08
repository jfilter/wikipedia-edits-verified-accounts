# Get All Revisions and Recent Changes for Verifed Users

For the German Wikipedia, we want to get contributions of [verified accounts](https://de.wikipedia.org/wiki/Kategorie:Benutzer:Verifiziert) to Wikipedia.

## Installation

1.  [install Python 3.6](http://docs.python-guide.org/en/latest/starting/installation/)
2.  [instal Pipenv](https://docs.pipenv.org/)
3.  After cloning, install dependencies with `pipenv install`

## Usage

1.  Get all verified user: [get_verified_users.py](get_verified_users.py)
2.  Get recent changes: [get_recent_changes_per_user.py](get_recent_changes_per_user.py)
3.  Get all revisions: [get_revisions_per_user.py](get_revisions_per_user.py)

We will have two CSV files for each user. One contains the recent changes and one contains the revisions.

## License

MIT.
