class calculator:
    """A calculator class"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiply two vectors"""
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(f'Dot product is: {result}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors"""
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] + V2[i]))
        print(f'Add Vector is: {result}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substract two vectors"""
        result = []
        for i in range(len(V1)):
            result.append(float(V1[i] - V2[i]))
        print(f'Sous Vector is: {result}')
