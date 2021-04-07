#!/bin/bash

cd ../../

grep -rli 'Project27' * | xargs -I@ sed -i '.bak' 's/Project27/\{\{\ site.brand\ \}\}/g' @

echo "String replacement done"
