import gzip  # read/write gzipped files
import os  # os routines
import re  # regex

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _, ngettext


class MinimumLengthValidator:
    """
    Validate whether the password is of a minimum length.
    """

    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "Password must contain at least %(min_length)d character.",
                    "Password must contain at least %(min_length)d characters.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "Password must contain at least %(min_length)d character.",
            "Password must contain at least %(min_length)d characters.",
            self.min_length
        ) % {'min_length': self.min_length}


class NumericPasswordValidator:
    """
    Validate whether the password is alphanumeric.
    """

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("Password must not be entirely numeric."),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _("Password must not be entirely numeric.")


class CommonPasswordValidator:
    """
    Validate whether the password is a common password.

    The password is rejected if it occurs in a provided list, which may be
    gzipped.
    <or> Mark Bunett's 10 Million Common Passwords:
    https://xato.net/today-i-am-releasing-ten-million-passwords-b6278bbe7495
    <or> Django's 20k Common Passwords:
    https://github.com/django/django/blob/master/django/contrib/auth/common-passwords.txt.gz
    """
    DEFAULT_PASSWORD_LIST_PATH = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'common-passwords.txt.gz'
    )

    def __init__(self, password_list_path=DEFAULT_PASSWORD_LIST_PATH):
        try:
            with gzip.open(password_list_path) as f:
                common_passwords_lines = f.read().decode().splitlines()
        except IOError:
            with open(password_list_path) as f:
                common_passwords_lines = f.readlines()

        self.passwords = {p.strip() for p in common_passwords_lines}

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _("Password must not be a commonly used password."),
                code='password_too_common',
            )

    def get_help_text(self):
        return _("Password must not be a commonly used password.")


class NumberValidator:
    """
    Validate whether the password contains at least specified number of digits,
    defaults to 1 digit
    """

    def __init__(self, min_num=1):
        self.min_num = min_num

    def validate(self, password, user=None):
        if not len(re.findall('[0-9]', password)) >= self.min_num:
            raise ValidationError(
                ngettext(
                    "Password must contain at least %(min_num)d digit [0-9].",
                    "Password must contain at least %(min_num)d digits [0-9].",
                    self.min_num
                ),
                code='password_no_number',
                params={'min_num': self.min_num},
            )

    def get_help_text(self):
        return ngettext(
            "Password must contain at least %(min_num)d digit [0-9].",
            "Password must contain at least %(min_num)d digits [0-9].",
            self.min_num
        ) % {'min_num': self.min_num}


class UppercaseValidator:
    """
    Validate whether the password contains at least specified number of
    uppercase characters,
    defaults to 1 uppercase character
    """

    def __init__(self, min_upper=1):
        self.min_upper = min_upper

    def validate(self, password, user=None):
        if not len(re.findall('[A-Z]', password)) >= self.min_upper:
            raise ValidationError(
                ngettext(
                    "Password must contain at least %(min_upper)d uppercase "
                    + "letter [A-Z].",
                    "Password must contain at least %(min_upper)d upppercase "
                    + "letters [A-Z].",
                    self.min_upper
                ),
                code='password_no_upper',
                params={'min_upper': self.min_upper},
            )

    def get_help_text(self):
        return ngettext(
            "Password must contain at least %(min_upper)d uppercase letter "
            + "[A-Z].",
            "Password must contain at least %(min_upper)d uppercase letters "
            + "[A-Z].",
            self.min_upper
        ) % {'min_upper': self.min_upper}


class LowercaseValidator:
    """
    Validate whether the password contains at least specified number of
    lowercase characters,
    defaults to 1 lowercase character
    """

    def __init__(self, min_lower=1):
        self.min_lower = min_lower

    def validate(self, password, user=None):
        if not len(re.findall('[a-z]', password)) >= self.min_lower:
            raise ValidationError(
                ngettext(
                    "Password must contain at least %(min_lower)d lowercase "
                    + "letter [a-z].",
                    "Password must contain at least %(min_lower)d lowercase "
                    + "letters [a-z].",
                    self.min_lower
                ),
                code='password_no_upper',
                params={'min_lower': self.min_lower},
            )

    def get_help_text(self):
        return ngettext(
            "Password must contain at least %(min_lower)d lowercase letter "
            + "[a-z].",
            "Password must contain at least %(min_lower)d lowercase letters "
            + "[a-z].",
            self.min_lower
        ) % {'min_lower': self.min_lower}
