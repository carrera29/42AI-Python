class Evaluator:
    def enumerate_evaluate(coefs, words):
        if len(coefs) == len(words):
            result = 0
            for i, word in enumerate(words):
                result += coefs[i] * len(word)
            return result
        else:
            "Error, diff shapes"

    def zip_evaluate(coefs, words):
        if len(coefs) == len(words):
            result = 0
            for i, word in zip(coefs, words):
                result += i * len(word)
            return result
        else:
            "Error, diff shapes"

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

num1 = Evaluator.zip_evaluate(coefs, words)
num = Evaluator.zip_evaluate(coefs, words)
print (num1, num)