#include <Windows.h>
#include <stdio.h>

const int MazeHeight = 9;
const int MazeWidth = 9;

char Maze[MazeHeight][MazeWidth + 1] =
{
    "|||||||||",
    "|   |   |",
    "  ||| | |",
    "| |   | |",
    "| | | |||",
    "|   | | |",
    "| ||| | |",
    "|   |   |",
    "||||||| |",
};

const char Wall = '|';
const char Free = ' ';
const char SomeDude = '*';

class koordinat
{
public:
    int X;
    int Y;
    koordinat(int x = 0, int y = 0) { X = x, Y = y; }
    koordinat(const koordinat &koordinat) { X = koordinat.X; Y = koordinat.Y; }
};

koordinat StartingPoint(0, 2);
koordinat EndingPoint(7, 8);

void PrintDaMaze()
{
    for (int Y = 0; Y < MazeHeight; Y++)
    {
        printf("%s\n", Maze[Y]);
    }
    printf("\n");
}

bool Solve(int X, int Y)
{
    Maze[Y][X] = SomeDude;

    PrintDaMaze();
    Sleep(500);
	system("CLS");

    if (X == EndingPoint.X && Y == EndingPoint.Y)
    {
        return true;
    }

    if (X > 0 && Maze[Y][X - 1] == Free && Solve(X - 1, Y))
    {
        return true;
    }
    if (X < MazeWidth && Maze[Y][X + 1] == Free && Solve(X + 1, Y))
    {
        return true;
    }
    if (Y > 0 && Maze[Y - 1][X] == Free && Solve(X, Y - 1))
    {
        return true;
    }
    if (Y < MazeHeight && Maze[Y + 1][X] == Free && Solve(X, Y + 1))
    {
        return true;
    }

    Maze[Y][X] = Free; // backtracking

    return false;
}

void main()
{
    if (Solve(StartingPoint.X, StartingPoint.Y))
    {
        PrintDaMaze();
		printf("\nSolution found\n");
    }
    else
    {
        printf("Solution not found\n");
    }
}