{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/venkatram0502/python_record/blob/main/Copy_of_Welcome_To_Colab.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sentence = input(\"Enter a sentence: \")\n",
        "# Count words\n",
        "words = sentence.split()\n",
        "num_words = len(words)\n",
        "# Initialize counters\n",
        "num_digits = 0\n",
        "num_uppercase = 0\n",
        "num_lowercase = 0\n",
        "# Count digits and letters\n",
        "for char in sentence:\n",
        "    if char.isdigit():\n",
        "        num_digits += 1\n",
        "    elif char.isupper():\n",
        "        num_uppercase += 1\n",
        "    elif char.islower():\n",
        "        num_lowercase += 1\n",
        "# Print results after the loop\n",
        "print(\"Number of words:\", num_words)\n",
        "print(\"Number of digits:\", num_digits)\n",
        "print(\"Number of uppercase letters:\", num_uppercase)\n",
        "print(\"Number of lowercase letters:\", num_lowercase)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8d-9Dd0CTABH",
        "outputId": "e607bc43-6bf6-4259-eed8-47657f2a02d8"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a sentence: Python Program 123\n",
            "Number of words: 3\n",
            "Number of digits: 3\n",
            "Number of uppercase letters: 2\n",
            "Number of lowercase letters: 11\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
