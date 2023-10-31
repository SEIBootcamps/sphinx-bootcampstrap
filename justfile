git-hooks:
  @echo "Installing pre-commit and other Git hooks..."
  pre-commit install

build: css sphinx

sphinx:
  @rm -rf examples/_build
  @poetry run sphinx-build -b html -d examples/_build/doctrees -n examples/ examples/_build/html

css:
  yarn run build