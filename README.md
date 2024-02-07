# WhiteLabel-MS-Python

This is a micro-servce template for Python that uses the best serverless principles:

- Simplicity
- Modularity
- TDD
- Hexagonal Architecture

## Why?

When developig a serverless Architecture, you can use this infrastructure as a Lambda Function, an AWS Fargate or a Lambda Container with unit testing and some or none modifications. This helps developing fast-paced and scalable applications.

## Run tests

```bash
python3 -m unittest discover -s useCases/ -v
```

## Create new UseCase

```bash
python3 CLI/index.py
```
