from block import Block
blockchain = []

genesis_block = Block("The first blcok in the chain...", ["Nate to Brian 2 BTC", "Joel to Nate 10 BTC"])

second_block = Block(genesis_block.block_hash, ['Nate to Sam 0.5 BTC'])

third_block = Block(second_block.block_hash, ['A to B 5 BTC', 'L to R 15 BTC'])

print(f"Block Hash - Genesis Block: {genesis_block.block_hash}")
print(f'Block Hash - Second Block: {second_block.block_hash}')
print(f'Block Hash - Third Block: {third_block.block_hash}')