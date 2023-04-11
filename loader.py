def load_data(data_path):
    maze = []
    path = []
    with open(data_path, 'r') as f:
        for line in f:
            if '#' in line or '.' in line:
                maze.append(list(line.strip()))
            elif ',' in line:
                try:
                    path.append(tuple(int(i) for i in line.split(',')))
                except ValueError:
                    print('Arquivo de dados inválido')
    return maze, path
