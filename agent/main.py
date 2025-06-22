import logging
import os
import asyncio

import click

from agent import OrangeTheoryAgent
from task_manager import AgentTaskManager
from google_a2a.common.server import A2AServer
from google_a2a.common.types import (
    AgentCapabilities,
    AgentCard,
    AgentSkill,
)
from google_a2a.common.utils.push_notification_auth import PushNotificationSenderAuth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(host, port):
    """Starts the Orange Theory Agent server."""
    try:
    
        capabilities = AgentCapabilities(streaming=False, pushNotifications=True)
        skill = AgentSkill(
            id='otf_assistant',
            name='Orange Theory Assistant',
            description='Helps with Orange Theory Fitness bookings, classes, stats, and studio information.',
            tags=['otf', 'fitness', 'bookings', 'classes', 'stats', 'studio'],
            examples=['Book me into a class tomorrow', 'Show my stats for last month', 'Find studios near me'],
        )
        agent_card = AgentCard(
            name='Orange Theory Agent',
            description='Helps with Orange Theory Fitness bookings, classes, stats, and studio information.',
            url=f'http://{host}:{port}/',
            version='1.0.0',
            defaultInputModes=OrangeTheoryAgent.SUPPORTED_CONTENT_TYPES,
            defaultOutputModes=OrangeTheoryAgent.SUPPORTED_CONTENT_TYPES,
            capabilities=capabilities,
            skills=[skill],
        )

        notification_sender_auth = PushNotificationSenderAuth()
        notification_sender_auth.generate_jwk()
        agent = OrangeTheoryAgent()
    
        server = A2AServer(
            agent_card=agent_card,
            task_manager=AgentTaskManager(
                agent= agent,
                notification_sender_auth=notification_sender_auth,
            ),
            host=host,
            port=port,
        )

        server.app.add_route(
            '/.well-known/jwks.json',
            notification_sender_auth.handle_jwks_endpoint,
            methods=['GET'],
        )

        logger.info(f'Starting server on {host}:{port}')
        server.start()
    except Exception as e:
        logger.error(f'An error occurred during server startup: {e}')
        exit(1)



main("0.0.0.0", 10000)