from multiprocessing import Process, Pipe

def sender(conn):
    data=("Hello! This is the sender.",)
    conn.send(data)
    conn.close()

def receiver(conn):
    data=conn.recv()
    print("Received : ",data[0])
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    sender_process = Process(target=sender, args=(parent_conn,))
    receiver_process = Process(target=receiver, args=(child_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()