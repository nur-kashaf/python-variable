{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOCvTQhK0hbXoFRwb0XVhEe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/nur-kashaf/python-variable/blob/main/condition.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xXHJ7xJbrG2J",
        "outputId": "6cf83d75-26fe-4f1d-f627-839c37822659"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the number is even\n"
          ]
        }
      ],
      "source": [
        "num = 4\n",
        "if num %4 == 0:\n",
        "   print(\"the number is even\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = 2\n",
        "if num % 4 ==0:\n",
        "  print (\"the number is even\")\n",
        "if num % 7 ==2:\n",
        "   print(\"the number is odd\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xDuFz4FdrSaU",
        "outputId": "366e5bcd-8726-44e2-803e-7e5f8e79443f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the number is odd\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = 7\n",
        "if num %3 == 1:\n",
        "  print(\"the number is odd\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uBDoNybvtJqK",
        "outputId": "506ed898-a1fc-4f60-b2a4-e24505030a06"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the number is odd\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = 7\n",
        "if num % 3 ==1:\n",
        "  print(\"the number is odd\")\n",
        "if num % 3==0:\n",
        "  print(\"the number is even\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GzV75Ubovvys",
        "outputId": "fe09ebbd-4912-409a-9de6-efd5ceb3fe32"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "the number is odd\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 40\n",
        "if age>= 18:\n",
        "  print(\"senior citizen\")\n",
        "if age<= 40:\n",
        "    print(\"young citizen\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tfKMPv3I65dP",
        "outputId": "3aa57fa6-ca4c-43c1-e2e4-a69f6fdb508f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "senior citizen\n",
            "young citizen\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age =30\n",
        "if age >=18:\n",
        "     print(\"senior citizen\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_XbMk3AJwoRg",
        "outputId": "7fed0428-703a-47b9-c26a-f88ca717d729"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "senior citizen\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 30\n",
        "if age >=18:\n",
        "  print(\"young citizen\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Td_eK3Y16Z-a",
        "outputId": "3445cd78-38b9-47f0-b31f-3e9521ccdb7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "young citizen\n"
          ]
        }
      ]
    }
  ]
}