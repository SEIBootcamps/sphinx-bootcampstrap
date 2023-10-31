git-hooks:
  @echo "Installing pre-commit and other Git hooks..."
  pre-commit install

build: css sphinx

sphinx:
  @rm -rf examples/kitchen-sink/_build
  @poetry run sphinx-build -b html -d examples/kitchen-sink/_build/doctrees -n examples/kitchen-sink examples/kitchen-sink/_build/html

css:
  yarn run build