#include <iostream>
#include <string>
#include <cctype>
#include <vector>

enum class TokenType {
    Number,
    PlusOperator,
    MinusOperator,
    MultiplyOperator,
    DivideOperator,
    EndOfExpression,
    Invalid
};

struct Token {
    TokenType type;
    std::string value;
};

class Lexer {
public:
    Lexer(const std::string& inputExpression) : expression(inputExpression), index(0) {}

    Token getNextToken() {
        Token token;

        while (index < expression.length() && std::isspace(expression[index])) {
            ++index;
        }

        if (index >= expression.length()) {
            token.type = TokenType::EndOfExpression;
            return token;
        }

        char currentChar = expression[index];

        if (std::isdigit(currentChar)) {
            size_t start = index;
            while (index < expression.length() && std::isdigit(expression[index])) {
                ++index;
            }
            token.value = expression.substr(start, index - start);
            token.type = TokenType::Number;
        }
        else if (currentChar == '+') {
            token.value = "+";
            token.type = TokenType::PlusOperator;
            ++index;
        }
        else if (currentChar == '-') {
            token.value = "-";
            token.type = TokenType::MinusOperator;
            ++index;
        }
        else if (currentChar == '*') {
            token.value = "*";
            token.type = TokenType::MultiplyOperator;
            ++index;
        }
        else if (currentChar == '/') {
            token.value = "/";
            token.type = TokenType::DivideOperator;
            ++index;
        }
        else {
            token.value = std::string(1, currentChar);
            token.type = TokenType::Invalid;
            ++index;
        }

        return token;
    }

private:
    std::string expression;
    size_t index;
};

class Parser {
public:
    Parser(Lexer& lexerInstance) : lexer(lexerInstance) {
        currentToken = lexer.getNextToken();
    }

    int evaluateExpression() {
        int result = parseTerm();

        while (currentToken.type == TokenType::PlusOperator || currentToken.type == TokenType::MinusOperator) {
            if (currentToken.type == TokenType::PlusOperator) {
                currentToken = lexer.getNextToken();
                result += parseTerm();
            }
            else if (currentToken.type == TokenType::MinusOperator) {
                currentToken = lexer.getNextToken();
                result -= parseTerm();
            }
        }

        return result;
    }

private:
    Lexer& lexer;
    Token currentToken;

    int parseTerm() {
        int result = parseFactor();

        while (currentToken.type == TokenType::MultiplyOperator || currentToken.type == TokenType::DivideOperator) {
            if (currentToken.type == TokenType::MultiplyOperator) {
                currentToken = lexer.getNextToken();
                result *= parseFactor();
            }
            else if (currentToken.type == TokenType::DivideOperator) {
                currentToken = lexer.getNextToken();
                int divisor = parseFactor();
                if (divisor == 0) {
                    std::cerr << "Error: Division by zero!" << std::endl;
                    exit(1);
                }
                result /= divisor;
            }
        }

        return result;
    }

    int parseFactor() {
        if (currentToken.type == TokenType::Number) {
            int value = std::stoi(currentToken.value);
            currentToken = lexer.getNextToken();
            return value;
        }
        else {
            std::cerr << "Error: Expected a number but found an invalid token!" << std::endl;
            exit(1);
        }
    }
};

int main() {
    std::string expression;

    std::cout << "Expression: ";
    std::getline(std::cin, expression);

    Lexer lexer(expression);
    Parser parser(lexer);

    try {
        int result = parser.evaluateExpression();
        std::cout << "Result: " << result << std::endl;
    }
    catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
