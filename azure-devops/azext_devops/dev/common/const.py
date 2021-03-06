# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure.cli.core._environment import get_config_dir

# Config directory
AZ_CLI_GLOBAL_CONFIG_DIR = get_config_dir()
_AZ_DEVOPS_CONFIG_DIR_NAME = 'azuredevops'
AZ_DEVOPS_DEFAULT_CONFIG_DIR = os.path.join(AZ_CLI_GLOBAL_CONFIG_DIR, _AZ_DEVOPS_CONFIG_DIR_NAME)


# Environment Variables
CLI_ENV_VARIABLE_PREFIX = 'AZURE_DEVOPS_EXT_'
AZ_DEVOPS_CONFIG_DIR_ENVKEY = CLI_ENV_VARIABLE_PREFIX + 'CONFIG_DIR'
AZ_DEVOPS_GITHUB_PAT_ENVKEY = CLI_ENV_VARIABLE_PREFIX + 'GITHUB_PAT'

# Config file constants
CONFIG_FILE_NAME = 'config'
DEFAULTS_SECTION = 'defaults'
DEVOPS_ORGANIZATION_DEFAULT = 'organization'
DEVOPS_TEAM_PROJECT_DEFAULT = 'project'
PAT_ENV_VARIABLE_NAME = CLI_ENV_VARIABLE_PREFIX + 'PAT'
AUTH_TOKEN_ENV_VARIABLE_NAME = CLI_ENV_VARIABLE_PREFIX + 'AUTH_TOKEN'

# Artifact tool variables
ARTIFACTTOOL_OVERRIDE_PATH_ENVKEY = CLI_ENV_VARIABLE_PREFIX + "ARTIFACTTOOL_OVERRIDE_PATH"
ARTIFACTTOOL_OVERRIDE_URL_ENVKEY = CLI_ENV_VARIABLE_PREFIX + "ARTIFACTTOOL_OVERRIDE_URL"
ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY = CLI_ENV_VARIABLE_PREFIX + "ARTIFACTTOOL_OVERRIDE_VERSION"
ARTIFACTTOOL_PAT_ENVKEY = CLI_ENV_VARIABLE_PREFIX + "ARTIFACTTOOL_PATVAR"

# Utility constants.
_TRUE_FALSE_SWITCH = ['true', 'false']
