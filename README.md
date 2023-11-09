# TicTacToe_MuhammadAhnafMaulana
# Module 6
## Permainan Tic Tac Toe (Best First Search)

#### Penjelasan
![alt text](https://github.com/nnooi/TicTacToe_MuhammadAhnafMaulana/blob/212f5103abe5bcdf8222939cb134a93b650d5b7e/src/Tree_TicTacToe.jpeg?raw=true)
Pada module 6 ini BSF digunakan mencapai solusi yang optimal. Pada modul ini memperlihatkan bagaimana membuat sebuah permainan tic tac toe. Initial state dari permainan ini adalah puzzle ukuran 8 yang tidak berisikan apa apa. Ketika pemain pertama menekan salah satu ubin, maka ubin tersebut akan diberikan tanda silang. Pemain kedua harus menghalangi pemain pertama untuk membuat tanda silang berjajaran baik secara vertikal, horizontal, atau diagonal. Permainan ini akan berakhir (goal state) ketika salah seorang pemain sudah menderetkan tanda meraka masing-masing baik secara vertikal, horizontal, atau diagonal. 

Solusi dari permasalahan ini dapat dilakukan dengan membuat topologi Tree, kemudian setiap langkah dari pemain pertama atau kedua akan menjadikan initial state selanjutnya, kemudian langkah tersebut akan dijadikan sebagai initial state yang baru sampai menemukan goal statenya. Ilustrasi penyelesaian masalah permainan tic tac toe ini dapat dilihat pada gambar di atas.

Best First Search sendiri merupakan algoritma pencarian yang untuk mengeksplorasi ruang pencarian, seperti struktur graf dan pohon. Algoritma ini didasarkan pada informasi dengan memilih simpul yang paling menjanjikan untuk dieksplorasi berdasarkan fungsi heuristik, Fungsi heuristiknya sendiri digunakan untuk mengestimasi biaya atau nilai yang terkait dengan setiap simpul dalam ruang pencarian. Fungsi ini memandu pencarian dengan memberikan informasi tentang simpul mana yang kemungkinan besar akan menuju solusi yang berhasil dan tetap menjaga antrian prioritas.

Berikut merupakan Pseudocode dari Best First Search untuk diimplementasikan di Permainan TicTacToe
 ```sh
Best-First-Search(Graph g, Node start)
    1) Create an empty PriorityQueue
       PriorityQueue pq;
    2) Insert "start" in pq.
       pq.insert(start)
    3) Until PriorityQueue is empty
          u = PriorityQueue.DeleteMin
          If u is the goal
             Exit
          Else
             Foreach neighbor v of u
                If v "Unvisited"
                    Mark v "Visited"                    
                    pq.insert(v)
             Mark u "Examined"                    
End procedure
```


## Tugas
- Tuliskan code permainan tic tac toe yang menggunakan algorithma Best First Search 

#### Jawab
- Code yang saya tuliskan merupakan code dari permainan tic tac toe yang menggunakan algoritma Best First Search dengan python dan GUInya menggunakan library tkinter. Dapat dilihat pada ([Source Code ](https://github.com/nnooi/TicTacToe_MuhammadAhnafMaulana/blob/212f5103abe5bcdf8222939cb134a93b650d5b7e/src/tictactoe.py))

Berikut merupakan hasil dari code yang dilakukan 
![alt text](https://github.com/nnooi/TicTacToe_MuhammadAhnafMaulana/blob/3784181d8939f02354783be35e994398b39d23ad/src/hasilprogram.jpeg?raw=true)
- Pada gambar di atas dijelaskan bagaimana program telah bekerja, Program bekerja dengan memainkan 2 mode yaitu player jalan awal atau komputer (ai) jalan awal. Ai digunakan untuk melakukan pencarian yang paling tepat pada permainan ini berdasarkan respon dari player dan algoritma dari ai yang digunakan merupakan Best First Search.
```sh
def evaluate_board():
    for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        a, b, c = combo
        if board[a] == board[b] == "O" and board[c] == " ":
            return c
        if board[b] == board[c] == "O" and board[a] == " ":
            return a
        if board[a] == board[c] == "O" and board[b] == " ":
            return b
    return None

# membuat pergerakan ai berdasarkan Best First Search Algoritma
def ai_move():
    best_move = None
    best_score = -float("inf")
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = evaluate_board()
            board[i] = " "
            
            if score is not None:
                if score > best_score:
                    best_score = score
                    best_move = i
    
    if best_move is not None:
        board[best_move] = "O"
        buttons[best_move].config(text="O", state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                result_label.config(text="It's a Draw!", )
            else:
                result_label.config(text="AI wins!", )
            for button in buttons:
                button.config(state="disabled")
    else:
      
        random_ai_move()

def random_ai_move():
    if " " in board:
        ai_choice = random.choice([i for i, val in enumerate(board) if val == " "])
        board[ai_choice] = "O"
        buttons[ai_choice].config(text="O", state="disabled", )
        winner = check_winner()
        if winner:
            if winner == "Draw":
                result_label.config(text="It's a Draw!", )
            else:
                result_label.config(text="AI wins!", )
            for button in buttons:
                button.config(state="disabled")

```
- Code diatas merupakan penerapan algoritma BFS dalam menentukan posisi yang paling optimal pada permainan tic tac toe. 
