#!/bin/bash

cd ../../docs/

grep -rli 'guide' * | xargs -I@ sed -i '.bak' 's/guide/guide/g' @

echo "String replacement done"
