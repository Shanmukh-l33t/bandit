# Regression example for B106 line reporting on multiline function calls:
# https://github.com/PyCQA/bandit/issues/1328
#
# The hardcoded password argument must be reported at the line of the
# keyword value, not at the line of the call.

def connect(host, port, password):
    pass


# Possible hardcoded password: 'blerg'
# Severity: Low   Confidence: Medium
# reported at the line of "blerg", not at the line of the call
connect(
    "example.com",
    5432,
    password="blerg",
)

# Possible hardcoded password: 's3cret'
# Severity: Low   Confidence: Medium
# reported at the line of "s3cret", not at the line of the call
connect(
    host="example.com",
    port=5432,
    password="s3cret",
)
