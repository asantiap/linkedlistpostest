class Node: 
  def __init__(self, data, kode, nama): 
    self.data = data
    self.kode = kode
    self.nama = nama
    self.next = None
 
class LinkedList: 
  def __init__(self): 
    self.head = None 
     
  def append(self, kode, nama): 
    # Menambah node baru ke akhir linked list 
    new_node = Node(None, kode, nama) 
    if self.head is None: 
        self.head = new_node 
    else:
        current = self.head 
        while current.next: 
            current = current.next 
        current.next = new_node 
     
  def prepend(self, kode, nama): 
    # Menambah node baru ke awal linked list 
    new_node = Node(None, kode, nama) 
    new_node.next = self.head 
    self.head = new_node 
     
  def delete(self, kode): 
    # Menghapus node dari linked list 
    current = self.head 
    if current and current.kode == kode: 
      self.head = current.next 
      current = None 
      return 
    prev = None 
    while current and current.kode != kode: 
      prev = current 
      current = current.next 
    if current is None: 
      return 
    prev.next = current.next 
    current = None 
     
  def print_list(self): 
    # Mencetak semua elemen dalam linked list 
    current = self.head 
    while current: 
      print("="*100)
      print("Kode booking:", current.kode, "\nNama:", current.nama)
      print("="*100)
      current = current.next

a = LinkedList()
def hps():
    a.print_list()
    x = int(input("Masukkan kode booking yang ingin dihapus: " ))
    a.delete(x)
    a.print_list()

def tmbh():
    # for i in range(3):
    # while True:
        kode = int(input("Masukkan kode booking: "))
        nama = input("Masukkan nama anda: ")
        a.append( kode,nama)
        a.print_list()

def menu ():
    while True:
        print(f"""
        ==============================
        |             Menu           |
        ==============================
        |           {"1. Tambah"}        |
        |           {"2. Hapus"}         |
        ===============================""")
        menu = input("pilih menu :")
        if menu == "1":
            tmbh()
        elif menu == "2":
            hps()

menu()