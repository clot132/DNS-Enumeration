import dns.resolver
target = input("Enter the Domain: ")
records = ['A','AAAA','CNAME','MX','TXT','SOA']

resolver = dns.resolver.Resolver()

for rec in records:
    try:
        ans = resolver.resolve(target,rec)
    except dns.resolver.NoAnswer:
        continue

print(f'{records} records for {target}')

for a in ans:
    print(f'{a}')