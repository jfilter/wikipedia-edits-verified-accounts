# Get All Revisions and Recent Changes for Verifed Users

For the German Wikipedia, we want to get contributions of [verified accounts](https://de.wikipedia.org/wiki/Kategorie:Benutzer:Verifiziert) to Wikipedia.

## Installation

1.  [install Python 3.6](http://docs.python-guide.org/en/latest/starting/installation/)
2.  [install Pipenv](https://docs.pipenv.org/)
3.  After cloning, install dependencies with Pipenv: `git clone https://github.com/jfilter/wikipedia-edits-verified-accounts && cd wikipedia-edits-verified-accounts && pipenv install`

## Usage

1.  Get all verified user: [`pipenv run python get_verified_users.py`](get_verified_users.py)
2.  Get recent changes: [`pipenv run python get_recent_changes_per_user.py`](get_recent_changes_per_user.py)
3.  Get all revisions: [`pipenv run python get_revisions_per_user.py`](get_revisions_per_user.py)

We will have two folders: One contains the recent changes and one contains the revisions, one file for each user. To merge the files, you can use [megrge_csv.py](merge_csv.py).

## License

MIT.
