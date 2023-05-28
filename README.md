# 십이장기
본 프로젝트는 "`더 지니어스`"의 게임 중 하나로, 더 지니어스 시즌3 블랙가넷과 시즌4 그랜드 파이널에서 각각 2번, 1번 진행되었던 데스매치게임으로 일본의 `동물장기`를 변형한 게임입니다. 🐷

---
## 룰
 - 십이장기는 가로 4칸, 세로 3칸 총 12칸으로 이루어진 게임 판에서 진행되며 플레이어들의 바로 앞쪽 3칸이 각자의 진영이 된다.

  - 4가지 종류의 말이 1개씩 주어지며 각 말은 지정된 위치에 놓인 상태로 게임을 시작한다.

  - 게임이 시작되면 선 플레이어부터 말 1개를 1칸 이동시킬 수 있다. 말을 이동시켜 상대방의 말을 잡은 경우, 해당 말을 포로로 잡게 되며 포로로 잡은 말은 다음 턴부터 자신의 말로 사용할 수 있다.

  - 게임 판에 포로로 잡은 말을 내려놓는 행동도 턴을 소모하는 것이며 이미 말이 놓여진 곳이나 상대의 진영에는 말을 내려놓을 수 없다.

  - 상대방의 후(侯)를 잡아 자신의 말로 사용할 경우에는 자(子)로 뒤집어서 사용해야 한다.

  - 게임은 한 플레이어가 상대방의 왕(王)을 잡으면. 혹은 왕(王)이 상대방의 진영에 들어가 자신의 턴이 다시 돌아올 때까지 한 턴을 버틸 경우. 해당 플레이어의 승리로 종료된다.

---
## 개발문서🎮
본 패키지는 `python`으로 제작되었습니다. 
### Move

말의 이동을 묶어주는 클래스입니다. 기본적으로 내장 클래스입니다. 접근하실 필요가 없습니다. 😋😊

### Move.\_\_init\_\_
```python
import Kchess12
Move(Start, End)
```

옵션은 아래를 참고. 
| Option   | Value  | Required |
| :------- | :----: | :------: |
| start | tuple[int, int] |    O     |
| end    | tuple[int, int] |    O     |
- `start`: 시작좌푯값을 지정합니다.
- `end`: 도착좌푯값을 지정합니다.


---

### Player

게임을 하는 플레이어 클래스입니다. 초기값으로 두명의 플레이어가 있어야합니다. 하나의 플레이어는 pitch값을 1로 나머지 한 명의 플레이어는 pitch값을 -1로 주세요. pitch는 진행방향을 의미합니다.


> 진행방향 :  >>> == 1,<br> 진행방향: <<< == -1 

### Player.\_\_init\_\_
```python
import Kchess12
Player(pitch)
```
옵션은 아래를 참고. 
| Option   | Value  | Required |
| :------- | :----: | :------: |
| pitch | int |    O    |

- `pitch`: 플레이어가 바라볼 방향을 지정합니다.

---

### Piece

기물에 관련한 클래스입니다. 각 기물에 대한 상속을 받는 클래스입니다.


### Player.setPos
```python
import Kchess12
p = Piece()
p.setPos(pos)
```
기물의 위치를 절대위치로 지정합니다.
옵션은 아래를 참고. 
| Option   | Value  | Required |
| :------- | :----: | :------: |
| pos | tuple[int, int] |    O    |

- `pos`: 기물이 있는 위치를 지정합니다.
---
### Player.getAbleMove
```python
import Kchess12
p = Piece()
p.getAbleMove(x,y)
```
현재말의 위치를 기준으로 상대적으로 어떤 위치로 이동 가능한 지를 반환합니다.
옵션은 아래를 참고. 
| Option   | Value  | Required |
| :------- | :----: | :------: |
| x | List |    O    |
| y | List |    O    |

- `x`: 기물의 이동이 가능한 칸의 x좌표의 상대값을 의미합니다
- `y`: 기물의 이동이 가능한 칸의 y좌표의 상대값을 의미합니다
---
### Player.goMove
```python
import Kchess12
p = Piece()
p.goMove(Move)
```
기물을 이동합니다
옵션은 아래를 참고. 
| Option   | Value  | Required |
| :------- | :----: | :------: |
| move | Kchess12.Move |    O    |

- `move`: 기물의 이동에 대한 정보입니다.
---
### Player.catched
```python
import Kchess12
p = Piece()
p.goMove(attacker)
```
기물이 잡혔을 때 호출 되야하는 함수입니다. 
옵션은 아래를 참고. 
| Option   | Value  | Required |
| :------- | :----: | :------: |
| attacker | Kchess12.Player |    O    |

- `attacker`: 기물을 잡은 플레이어에 대한 정보입니다.


---
### Board
게임판에 대한 클래스입니다. 기본적인 게임을 다루는 클래스입니다.

### Board.\_\_init\_\_
보드를 생성합니다.
옵션은 아래를 참고.
| Option   | Value  | default | Required |
| :------- | :----: | :------: | :------: |
| pitch | int |    0    | X |

---
### Board.boardInitialize
```python
import Kchess12
positicePlayer = Player(1)
negativePlayer = Player(-1)
board = Board(positicePlayer, negativePlayer)
```
보드를 초기화합니다.
옵션은 아래를 참고.
| Option   | Value  | Required |
| :------- | :----: | :------: |
| positicePlayer | Kchess12.Player |    O    |
| negativePlayer | Kchess12.Player |    O    |

- `positicePlayer`: pitch값이 1인 플레이어를 의미합니다
- `negativePlayer`: pitch값이 -1인 플레이어를 의미합니다

---
### Board.boardInitialize
```python
import Kchess12
positicePlayer = Player(1)
negativePlayer = Player(-1)
board = Board(positicePlayer, negativePlayer)
board.boardInitialize()
```
보드를 초기화합니다.
옵션은 아래를 참고.
| Option   | Value  | Required |
| :------- | :----: | :------: |
| positicePlayer | Kchess12.Player |    O    |
| negativePlayer | Kchess12.Player |    O    |

- `positicePlayer`: pitch값이 1인 플레이어를 의미합니다
- `negativePlayer`: pitch값이 -1인 플레이어를 의미합니다
---
### Board.getBoard
```python
import Kchess12
positicePlayer = Player(1)
negativePlayer = Player(-1)
board = Board(positicePlayer, negativePlayer)
board.boardInitialize()
print(board.getBoard())
```
보드를 가져옵니다. 빈 공간은 0으로, 빈공간이 아니라면 Piece 객체가 들어있습니다.
---
### Board.getSquare
```python
import Kchess12
positicePlayer = Player(1)
negativePlayer = Player(-1)
board = Board(positicePlayer, negativePlayer)
board.boardInitialize()
print(board.getSquare(x,y))
```
x,y좌표로 보드의 한 칸을 가져옵니다. 빈 공간은 0으로, 빈공간이 아니라면 Piece 객체가 들어있습니다.
| Option   | Value  | Required | MaxValue |
| :------- | :----: | :------: | :------: |
| x | int |    O    |  3  |
| y | int |    O    |  2  |

- `x`: x좌표를 입력해주세요.
- `y`: y좌표를 입력해주세요.

---
## 기물
- `왕王` -  자신의 진영 중앙에 위치하며 앞, 뒤, 좌, 우, 대각선 방향까지 모든 방향으로 이동이 가능하다.

- `상相` - 자신의 진영 왼쪽에 놓이며 대각선 4방향으로 이동할 수 있다.
- `장將` - 자신의 진영 오른쪽에 놓이는 말로 앞, 뒤와 좌, 우로 이동이 가능하다.
- `자子` - 왕의 앞에 놓이며 오로지 앞으로만 이동할 수 있다. 다만 상대방의 진영에 도착시에 `후侯`로 사용된다. 후(侯)는 대각선 뒤쪽 방향을 제외한 전 방향으로 이동할 수 있다.

### 개발
각 기물에 대한 것은 왕-King, 상-Sang, 장-Jang, 자-Ja 클래스로 정의 되어있습니다. 커스터마이징 게임을 하실 때 board 이니셜라이즈대신 사용하시면 됩니다.