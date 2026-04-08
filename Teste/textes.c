#include <iostream>
#include <string>
#include <vector>

using namespace std;

void exibirPalavra(const string& palavra, const vector<bool>& letrasCorretas) {
    for (size_t i = 0; i < palavra.size(); ++i) {
        if (letrasCorretas[i]) {
            cout << palavra[i] << " ";
        } else {
            cout << "_ ";
        }
    }
    cout << endl;
}

bool letraJaTentada(char letra, const vector<char>& tentativas) {
    for (char t : tentativas) {
        if (t == letra) {
            return true;
        }
    }
    return false;
}

int main() {
    string palavra = "programacao";  // Palavra secreta
    vector<bool> letrasCorretas(palavra.size(), false); // Vetor de letras corretas
    vector<char> tentativas;  // Vetor de tentativas feitas
    int tentativasRestantes = 6;  // Tentativas permitidas
    bool palavraCompleta = false;

    cout << "Bem-vindo ao jogo da forca!" << endl;

    while (tentativasRestantes > 0 && !palavraCompleta) {
        cout << "\nTentativas restantes: " << tentativasRestantes << endl;
        exibirPalavra(palavra, letrasCorretas);

        cout << "Digite uma letra: ";
        char letra;
        cin >> letra;

        if (letraJaTentada(letra, tentativas)) {
            cout << "Você já tentou essa letra!" << endl;
            continue;
        }

        tentativas.push_back(letra);

        bool letraEncontrada = false;
        for (size_t i = 0; i < palavra.size(); ++i) {
            if (palavra[i] == letra) {
                letrasCorretas[i] = true;
                letraEncontrada = true;
            }
        }

        if (!letraEncontrada) {
            --tentativasRestantes;
            cout << "Letra incorreta!" << endl;
        }

        // Verificar se a palavra foi completamente descoberta
        palavraCompleta = true;
        for (bool correta : letrasCorretas) {
            if (!correta) {
                palavraCompleta = false;
                break;
            }
        }
    }

    if (palavraCompleta) {
        cout << "\nParabéns! Você adivinhou a palavra: " << palavra << endl;
    } else {
        cout << "\nVocê perdeu! A palavra era: " << palavra << endl;
    }

    return 0;
}