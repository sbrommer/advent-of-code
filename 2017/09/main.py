def parse_garbage(stream):
    Σ = 0

    c, *stream = stream

    while c != '>':
        Σ += c != '!'

        if c == '!':
            stream = stream[1:]

        c, *stream = stream

    return stream, Σ


def parse_group(stream, depth=1):
    Σ_gr = depth
    Σ_ga = 0

    c, *stream = stream

    while c != '}':
        if c == '{':
            stream, dΣ_gr, dΣ_ga = parse_group(stream, depth+1)
            Σ_gr += dΣ_gr
            Σ_ga += dΣ_ga
        if c == '<':
            stream, dΣ = parse_garbage(stream)
            Σ_ga += dΣ

        c, *stream = stream
    return stream, Σ_gr, Σ_ga


stream = input()
print(*parse_group(stream[1:])[1:])
