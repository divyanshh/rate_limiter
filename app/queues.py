def get_remaining_queues(client_id, current_type):
    remaining_queues = ["Non sessional", "Sessional receive", "Sessional send"]
    remaining_queues.remove(current_type)
    return remaining_queues


def print_queue_status(limiter, client_id):
    queues = limiter.clients[client_id]
    message = f"Client {client_id}:"
    for message_type, timestamps in queues.items():
        total_messages = sum(timestamps[timestamp] for timestamp in timestamps)
        message += f" - {message_type}: {total_messages}"
    print(message)
