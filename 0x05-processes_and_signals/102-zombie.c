#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - infinite while
 * Return: Always 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: exit status
 */

int main(void)
{
	pid_t zombie_1, zombie_2, zombie_3, zombie_4, zombie_5;

	zombie_1 = fork();
	if (zombie_1 > 0)
		printf("Zombie process created, PID: %d\n", zombie_1);
	else
		exit(0);
	zombie_2 = fork();
	if (zombie_2 > 0)
		printf("Zombie process created, PID: %d\n", zombie_2);
	else
		exit(0);
	zombie_3 = fork();
	if (zombie_3 > 0)
		printf("Zombie process created, PID: %d\n", zombie_3);
	else
		exit(0);
	zombie_4 = fork();
	if (zombie_4 > 0)
		printf("Zombie process created, PID: %d\n", zombie_4);
	else
		exit(0);
	zombie_5 = fork();
	if (zombie_5 > 0)
		printf("Zombie process created, PID: %d\n", zombie_5);
	else
		exit(0);

	infinite_while();
	return (0);
}
