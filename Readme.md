# ATM

This project was created after I saw meme.

## Meme

![Original Meme](https://i.ibb.co/gtPGKzN/C9-FWy-CBgeyo.jpg)

## Problems

Standard deviation method is not optimal.
Example:
```
ATM Status:
    100$ - 3
    50$ - 3
    20$ - 2
    5$ - 2
Total sum - 500

Enter requested amount of money: 400

ATM Status:
    100$ - 1
    50$ - 0
    20$ - 0
    5$ - 0
Total sum - 100
```

Decision to dispense all money except 1x 100$ is not good as ATM cannot dispense any other amount of money now.
